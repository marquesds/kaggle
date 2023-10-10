from typing import Dict, Optional


class PassengerNuance:
    @staticmethod
    def pid(value: int) -> Dict[str, int]:
        if 0 <= value < 200:
            return {"X11": 1.0, "X12": 0, "X13": 0, "X14": 0, "X15": 0}
        elif 200 < value < 400:
            return {"X11": 0, "X12": 1.0, "X13": 0, "X14": 0, "X15": 0}
        elif 400 < value < 600:
            return {"X11": 0, "X12": 0, "X13": 1.0, "X14": 0, "X15": 0}
        elif 600 < value < 800:
            return {"X11": 0, "X12": 0, "X13": 0, "X14": 1.0, "X15": 0}
        else:
            return {"X11": 0, "X12": 0, "X13": 0, "X14": 0, "X15": 1.0}

    @staticmethod
    def pclass(value: int) -> Dict[str, int]:
        if value == 1:
            return {"X21": 1.0, "X22": 0, "X23": 0, "X24": 0}
        elif value == 2:
            return {"X21": 0, "X22": 1.0, "X23": 0, "X24": 0}
        elif value == 3:
            return {"X21": 0, "X22": 0, "X23": 1.0, "X24": 0}
        else:
            return {"X21": 0, "X22": 0, "X23": 0, "X24": 1.0}

    @staticmethod
    def sex(value: str) -> Dict[str, int]:
        if value.lower() == "male":
            return {"X31": 1.0, "X32": 0}
        else:
            return {"X31": 0, "X32": 1.0}

    @staticmethod
    def age(value: int) -> Dict[str, int]:
        if 0 < value < 10:
            return {
                "X41": 1.0,
                "X42": 0,
                "X43": 0,
                "X44": 0,
                "X45": 0,
                "X46": 0,
                "X47": 0,
                "X48": 0,
            }
        elif 10 < value < 20:
            return {
                "X41": 0,
                "X42": 1.0,
                "X43": 0,
                "X44": 0,
                "X45": 0,
                "X46": 0,
                "X47": 0,
                "X48": 0,
            }
        elif 20 < value < 30:
            return {
                "X41": 0,
                "X42": 0,
                "X43": 1.0,
                "X44": 0,
                "X45": 0,
                "X46": 0,
                "X47": 0,
                "X48": 0,
            }
        elif 30 < value < 40:
            return {
                "X41": 0,
                "X42": 0,
                "X43": 0,
                "X44": 1.0,
                "X45": 0,
                "X46": 0,
                "X47": 0,
                "X48": 0,
            }
        elif 40 < value < 50:
            return {
                "X41": 0,
                "X42": 0,
                "X43": 0,
                "X44": 0,
                "X45": 1.0,
                "X46": 0,
                "X47": 0,
                "X48": 0,
            }
        elif 50 < value < 60:
            return {
                "X41": 0,
                "X42": 0,
                "X43": 0,
                "X44": 0,
                "X45": 0,
                "X46": 1.0,
                "X47": 0,
                "X48": 0,
            }
        elif 60 < value < 70:
            return {
                "X41": 0,
                "X42": 0,
                "X43": 0,
                "X44": 0,
                "X45": 0,
                "X46": 0,
                "X47": 1.0,
                "X48": 0,
            }
        else:
            return {
                "X41": 0,
                "X42": 0,
                "X43": 0,
                "X44": 0,
                "X45": 0,
                "X46": 0,
                "X47": 0,
                "X48": 1.0,
            }

    @staticmethod
    def sibsp(value: int) -> Dict[str, int]:
        if 0 < value < 2:
            return {"X51": 1.0, "X52": 0, "X53": 0, "X54": 0}
        elif 2 < value < 4:
            return {"X51": 0, "X52": 1.0, "X53": 0, "X54": 0}
        elif 4 < value < 6:
            return {"X51": 0, "X52": 0, "X53": 1.0, "X54": 0}
        else:
            return {"X51": 0, "X52": 0, "X53": 0, "X54": 1.0}

    @staticmethod
    def parch(value: int) -> Dict[str, int]:
        if 0 < value < 2:
            return {"X61": 1.0, "X62": 0, "X63": 0}
        elif 2 < value < 4:
            return {"X61": 0, "X62": 1.0, "X63": 0}
        else:
            return {"X61": 0, "X62": 0, "X63": 1.0}

    @staticmethod
    def fare(value: float) -> Dict[str, int]:
        if 0 < value < 100:
            return {"X71": 1.0, "X72": 0, "X73": 0, "X74": 0, "X75": 0}
        elif 100 < value < 200:
            return {"X71": 0, "X72": 1.0, "X73": 0, "X74": 0, "X75": 0}
        elif 200 < value < 300:
            return {"X71": 0, "X72": 0, "X73": 1.0, "X74": 0, "X75": 0}
        elif 300 < value < 400:
            return {"X71": 0, "X72": 0, "X73": 0, "X74": 1.0, "X75": 0}
        else:
            return {"X71": 0, "X72": 0, "X73": 0, "X74": 0, "X75": 1.0}

    @staticmethod
    def embarked(value: Optional[str]) -> Dict[str, int]:
        if not value or not isinstance(value, str):
            return {"X81": 0, "X82": 0, "X83": 0, "X84": 1.0}

        if value.lower() == "c":
            return {"X81": 1.0, "X82": 0, "X83": 0, "X84": 0}
        elif value.lower() == "q":
            return {"X81": 0, "X82": 1.0, "X83": 0, "X84": 0}
        elif value.lower() == "s":
            return {"X81": 0, "X82": 0, "X83": 1.0, "X84": 0}
        else:
            return {"X81": 0, "X82": 0, "X83": 0, "X84": 1.0}

    def cabin(value: Optional[str]) -> Dict[str, int]:
        if not value or not isinstance(value, str):
            return {"X91": 0, "X92": 0, "X93": 0, "X94": 0, "X95": 0, "X96": 0, "X97": 1.0}

        if value.lower().startswith("a"):
            return {"X91": 1.0, "X92": 0, "X93": 0, "X94": 0, "X95": 0, "X96": 0, "X97": 0}
        elif value.lower().startswith("b"):
            return {"X91": 0, "X92": 1.0, "X93": 0, "X94": 0, "X95": 0, "X96": 0, "X97": 0}
        elif value.lower().startswith("c"):
            return {"X91": 0, "X92": 0, "X93": 1.0, "X94": 0, "X95": 0, "X96": 0, "X97": 0}
        elif value.lower().startswith("d"):
            return {"X91": 0, "X92": 0, "X93": 0, "X94": 1.0, "X95": 0, "X96": 0, "X97": 0}
        elif value.lower().startswith("e"):
            return {"X91": 0, "X92": 0, "X93": 0, "X94": 0, "X95": 1.0, "X96": 0, "X97": 0}
        elif value.lower().startswith("f"):
            return {"X91": 0, "X92": 0, "X93": 0, "X94": 0, "X95": 0, "X96": 1.0, "X97": 0}
        else:
            return {"X91": 0, "X92": 0, "X93": 0, "X94": 0, "X95": 0, "X96": 0, "X97": 1.0}
