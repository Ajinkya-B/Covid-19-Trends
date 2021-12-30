"""Evaluating the impact of COVID-19 on Canadians’ spending habits: prediction module

This module is responsible for creating a linear regression model with case counts
and spending index data, to make future predictions if there were to be another
pandemic 'wave'.

Copyright and Usage Information
===============================
This file is Copyright (c) 2021 Rafael Gacesa.
"""
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


class Predictor:
    _predictor: LinearRegression
    _cases: list[list]
    _csi: list[float]

    def __init__(self, cases: list, csi: list) -> None:
        self._cases = [[case, 1] for case in cases]
        self._csi = csi
        self._predictor = self.generate_predictor()

    def generate_predictor(self) -> LinearRegression:
        cases_train, _, csi_train, _ = train_test_split(self._cases, self._csi, random_state=0)
        predictor = LinearRegression()
        predictor.fit(cases_train, csi_train)
        return predictor

    def make_prediction(self, case_count: int) -> float:
        return self._predictor.predict([[case_count, 1]])[0]


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    python_ta.contracts.check_all_contracts()
    python_ta.check_all(config={
        'extra-imports': ['sklearn.model_selection', 'sklearn.linear_model'],
        'allowed-io': [],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import doctest

    doctest.testmod()
