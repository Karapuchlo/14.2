class LoggingMixin:
    def __init__(self, *args, **kwargs):
        print(f"Created object of class {self.__class__.__name__} with params: {args}, {kwargs}")
        super().__init__(*args, **kwargs)
