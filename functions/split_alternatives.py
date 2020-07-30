import logging

import numpy as np

def split_alternatives(df, column='label'):
    """ Splits labels that come with an alternative separated by '-' and adds
        a new column. Only one alternative is taken into account. `df` is
        mutated inplace.
    """
    regex = r"-(?!(\d|b|\#))" # <v2.2.0 works without lookahead: split_re='-'
    alternatives = df[column].str.split(regex, expand=True)
    if len(alternatives.columns) > 1:
        alt_name = f"alt_{column}"
        df.loc[:, column] = alternatives[0]
        df.insert(df.columns.get_loc(column)+1, alt_name, alternatives[2].fillna(np.nan)) # replace None by NaN
        if len(alternatives.columns) > 3:
            logging.warning(f"More than two alternatives are not taken into account: {alternatives[alternatives[2].notna()]}")
