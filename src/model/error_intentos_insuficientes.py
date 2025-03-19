class ErrorIntentosInsuficientes(Exception):

    def __init__(self):
        super().__init__(f"se han agotado las oportunidades para adivinar la palabra")
