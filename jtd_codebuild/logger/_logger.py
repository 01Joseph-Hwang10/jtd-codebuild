import abc


class Logger(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def debug(self, message: str, *args, **kwargs) -> None:
        pass

    @abc.abstractmethod
    def info(self, message: str, *args, **kwargs) -> None:
        pass

    @abc.abstractmethod
    def success(self, message: str, *args, **kwargs) -> None:
        pass

    @abc.abstractmethod
    def warning(self, message: str, *args, **kwargs) -> None:
        pass

    @abc.abstractmethod
    def error(self, message: str, *args, **kwargs) -> None:
        pass
