import main as m
import pytest as pt
import math
import logging
import logging.handlers


def test_czyMnozenieDzialaPoprawnie():
    a, b = 2, 2
    wynik = m.mnozenie(a, b)
    assert math.isclose(a * b, wynik) == True

def test_czyMnozenieZwracaFloata():
    assert type(m.mnozenie(2, 2)) == float

def test_czyDzielenieDzialaPoprawnie():
    a, b = 2, 2
    wynik = m.dzielenie(a, b)
    assert math.isclose(a / b, wynik) == True

def test_czyDzielenieZwracaFloata():
    assert type(m.dzielenie(2, 2)) == float

def test_czyDzielenieDzialaPoprawniePrzezZeroIZwracaNone():
    assert m.dzielenie(1, 0) is None

def test_czyOdejmowanieDzialaPoprawnie():
    a, b = 2, 2
    wynik = m.odejmowanie(a, b)
    assert math.isclose(a - b, wynik)

def test_czyOdejmowanieZwracaFloata():
    assert type(m.odejmowanie(2, 2)) == float

def test_czySredniaZwracaUwaga(caplog):
    m.srednia()

    assert len(caplog.records) == 1
    assert caplog.records[0].message == 'Uwaga'
