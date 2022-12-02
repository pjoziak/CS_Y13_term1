from abc import ABC, abstractmethod


class SwitchesAPI(ABC):
    a_time: float

    @abstractmethod
    def switch_on(self):
        ...

    @abstractmethod
    def switch_off(self):
        ...

    @abstractmethod
    def set_timer(self, a_time):
        ...

    @abstractmethod
    def get_timer(self):
        ...


class Microwave(SwitchesAPI):
    def switch_on(self):
        print('Switched on')

    def switch_off(self):
        print('Cannot be switched off')

    def get_timer(self):
        print('No way!')

    def set_timer(self, a_time):
        self.a_time = a_time


# switch = SwitchesAPI()
# switch.switch_on()
#
microwave: SwitchesAPI = Microwave()
microwave.switch_on()


