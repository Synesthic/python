class Television:
    '''
    A class that represents a television's power and mute statuses
    and its volume and channel values.
    '''
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        '''
        Method to initialize a television object
        with default statuses and values
        '''
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        '''
        Method that toggles the power status
        of a television object
        '''
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        '''
        Method that toggles the mute status
        of a television object
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self) -> None:
        '''
        Method that raises the value of a powered television object's channel,
        overflowing from the maximum channel to the minimum channel
        '''
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        '''
        Method that lowers the value of a powered television object's channel,
        underflowing from the minimum channel to the maximum channel
        '''
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        '''
        Method that raises the volume value on a powered television object,
        this does not raise/overflow volume above the maximum volume.
        Unmutes the television.
        :return:
        '''
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        '''
        Method that lowers the volume value on a powered television object,
        this does not lower/underflow volume below the minimum volume.
        Unmutes the television.
        :return:
        '''
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        '''
        Method that returns the power, channel, and volume of a television object
        in a formatted string. Note: if muted, the volume is reported as zero
        despite the stored value.
        :return: Power status, channel value, and volume value
        '''
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"