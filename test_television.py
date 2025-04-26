import pytest
from television import *

class Test:
    def setup_method(self):
        self.tv1 = Television()

    def teardown_method(self):
        del self.tv1

    def test_init(self):
        #Test: default values on object initialization
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_power(self):
        '''
        Test 1: tv on
        Test 2: tv off
        '''
        self.tv1.power()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 0"
        self.tv1.power()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_mute(self):
        '''
        Test 1: tv on, volume increase, and muted
        Test 2: tv on & unmuted
        Test 3: tv off & muted
        Test 4: tv off and unmuted
        '''
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.mute()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 0"
        self.tv1.mute()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 1"
        self.tv1.mute()
        self.tv1.power()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.tv1.power()
        self.tv1.mute()
        self.tv1.power()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 1"

    def test_channel_up(self):
        '''
        Test 1: tv off, channel increase
        Test 2: tv on, channel increase
        Test 3: tv on, channel increased beyond max channel
        '''
        self.tv1.channel_up()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.tv1.power()
        self.tv1.channel_up()
        assert self.tv1.__str__() == "Power = True, Channel = 1, Volume = 0"
        self.tv1.channel_up()
        self.tv1.channel_up()
        self.tv1.channel_up()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 0"

    def test_channel_down(self):
        '''
        Test 1: tv off, channel decreased
        Test 2: tv on, channel decreased beyond minimum
        '''
        self.tv1.channel_down()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.tv1.power()
        self.tv1.channel_down()
        assert self.tv1.__str__() == "Power = True, Channel = 3, Volume = 0"

    def test_volume_up(self):
        '''
        Test 1: tv off, volume increased
        Test 2: tv on, volume increased
        Test 3: tv on, volume at 1, but muted
        Test 4: tv on, volume increased to unmute
        Test 5: tv on, volume increased while at max
        '''
        self.tv1.volume_up()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.tv1.power()
        self.tv1.volume_up()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 1"
        self.tv1.mute()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 0"
        self.tv1.volume_up()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 2"
        self.tv1.volume_up()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 2"

    def test_volume_down(self):
        '''
        Test 1: tv off, volume decreased
        Test 2: tv on, volume maxed, then decreased once
        Test 3: tv on, volume maxed, muted
        Test 4: tv on, volume decreased from max to cause unmute
        Test 5: tv on, volume decreased while at minimum volume
        :return:
        '''
        self.tv1.volume_down()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.volume_up()
        self.tv1.volume_down()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 1"
        self.tv1.volume_up()
        self.tv1.mute()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 0"
        self.tv1.volume_down()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 1"
        self.tv1.volume_down()
        self.tv1.volume_down()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 0"