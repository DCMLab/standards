import logging

import numpy as np

def split_alternatives(df, column='label', logger=None):
    """ Splits labels that come with an alternative separated by '-' and adds
        a new column. Only one alternative is taken into account. `df` is
        mutated inplace.

    Parameters
    ----------
    df : :obj:`pandas.DataFrame`
        Dataframe where one column contains DCML chord labels.
    column : :obj:`str`, optional
        Name of the column that holds the harmony labels.
    logger : :obj:`logging.Logger`, optional
        Pass Logger object if you don't want to use the RootLogger.

    Example
    -------

    .. code-block:: python
        import pandas as pd
        labels = pd.read_csv('labels.csv')
        split_alternatives(labels)
    """
    if not logger:
        logger = logging.getLogger()

    regex = r"-(?!(\d|b|\#))" # <v2.2.0 labels work without lookahead: regex='-'
    alternatives = df[column].str.split(regex, expand=True)
    if len(alternatives.columns) > 1:
        alt_name = f"alt_{column}"
        df.loc[:, column] = alternatives[0]
        df.insert(df.columns.get_loc(column)+1, alt_name, alternatives[2].fillna(np.nan)) # replace None by NaN
        if len(alternatives.columns) > 3:
            logger.warning(f"More than two alternatives are not taken into account: {alternatives[alternatives[2].notna()]}")
