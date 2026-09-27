"""
vision_pratyaksha.py
--------------------
Computer-Vision bridge for Pratyaksha (direct perception), Sec. 42.

A real deployment would plug in an object-detection model (e.g. a
YOLOv8 CNN). To keep this engine dependency-free and 100%
reproducible offline, a MockVisionBackend is provided that simulates
a detector's structured output. Swap in a real model by implementing
the same VisionBackend.detect() interface and passing an instance to
PratyakshaVision(backend=...).
"""


class VisionBackend:
    """Interface every vision backend must implement."""

    def detect(self, image_input):
        """Must return a list of tuples:
            (object_name, {attribute_name: True/False, ...}, confidence)
        """
        raise NotImplementedError


class MockVisionBackend(VisionBackend):
    """
    Deterministic stand-in for a real CNN / YOLO model.

    Accepts either:
      (a) a dict that already looks like model output, e.g.:
          {
            "Mountain": {"attributes": {"smoke": True, "haze": False},
                         "confidence": 0.95}
          }
      (b) a plain string "pseudo-image description", scanned for known
          keywords (a crude stand-in for real recognition), e.g.
          "a mountain with thick smoke rising from its peak"
    """

    KEYWORD_MAP = {
        "mountain": ("Mountain", {}),
        "hill": ("Hill", {}),
        "smoke": (None, {"smoke": True}),
        "fire": (None, {"fire": True}),
        "flame": (None, {"fire": True}),
        "cloud": (None, {"clouds": True}),
        "rain": (None, {"rain": True}),
        "jar": ("Jar", {}),
        "pot": ("Jar", {}),
        "kitchen": ("Kitchen", {}),
    }

    def detect(self, image_input):
        if isinstance(image_input, dict):
            results = []
            for obj_name, payload in image_input.items():
                attrs = payload.get("attributes", {})
                conf = payload.get("confidence", 1.0)
                results.append((obj_name, attrs, conf))
            return results
        if isinstance(image_input, str):
            text = image_input.lower()
            detected_object = None
            attrs = {}
            for kw, (obj_name, attr_updates) in self.KEYWORD_MAP.items():
                if kw in text:
                    if obj_name:
                        detected_object = obj_name
                    attrs.update(attr_updates)
            if detected_object is None:
                if not attrs:
                    return []  # nothing recognisable at all
                detected_object = "UnknownObject"
            return [(detected_object, attrs, 0.9)]
        raise TypeError(
            "image_input must be a dict of structured detections or a "
            "descriptive string for the MockVisionBackend."
        )


class PratyakshaVision:
    """Feeds a vision backend's detections into the WorldModel as
    Pratyaksha (perception) facts -- the strongest pramana."""

    def __init__(self, backend=None):
        self.backend = backend or MockVisionBackend()

    def perceive_image(self, world, image_input, confidence_threshold=0.5,
                        verbose=True):
        detections = self.backend.detect(image_input)
        accepted = []
        if not detections:
            if verbose:
                print("[Vision] No recognisable objects/attributes detected.")
            return accepted
        for obj_name, attrs, conf in detections:
            if conf < confidence_threshold:
                if verbose:
                    print(f"[Vision] Skipping '{obj_name}' "
                          f"(confidence {conf:.2f} < {confidence_threshold}).")
                continue
            if not world.locus_exists(obj_name):
                world.facts.setdefault(obj_name, {})
            for attr, val in attrs.items():
                world.set_fact(obj_name, attr, val, source="pratyaksha")
                accepted.append((obj_name, attr, val, conf))
                if verbose:
                    verb = "possesses" if val else "lacks"
                    print(f"[Vision->Pratyaksha] Detected (conf={conf:.2f}): "
                          f"'{obj_name}' {verb} '{attr}'.")
        return accepted
