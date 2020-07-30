import re, logging

from split_alternatives import split_alternatives

def split_labels(df, regex, column='label', cols={}, dropna=False, **kwargs):
    """ Split harmony labels complying with the DCML syntax into columns holding their various features.

    Parameters
    ----------
    df : :obj:`pandas.DataFrame`
        Dataframe where one column contains DCML chord labels.
    regex : :obj:`re.Pattern`
        Compiled regular expression used to split the labels. It needs to have named groups.
        The group names are used as column names.
    column : :obj:`str`, optional
        Name of the column that holds the harmony labels.
    dropna : :obj:`bool`, optional
        Pass True if you want to drop rows where `column` is NaN/<NA>
    """

    assert regex.__class__ == re.compile('').__class__, "Compile regular expression using re.compile()"
    df = df.copy()
    if df[column].isna().any():
        if dropna:
            logging.debug(f"Removing NaN values from label column {column}...")
            df = df[df[column].notna()]
        else:
            logging.warning(f"{column} contains NaN values.")

    logging.debug(f"Splitting alternative annotations...")
    split_alternatives(df=df, column=column)

    logging.debug("Applying RegEx to labels...")
    spl = df[column].str.extract(regex, expand=True)
    features = regex.groupindex.keys()
    df[:, features] = spl[features]
    mistakes = df.numeral.isna() & df[column].notna()
    if mistakes.any():
        logging.warning(f"The following chords could not be parsed:\n{df.loc[mistakes, :column]}")
    return df

import pandas as pd
from get_regex import get_regex
labels = pd.read_csv('/home/hentsche/Documents/Code/tmp/labels.csv')
regex = get_regex('docs')
test = labels[~labels.label.str.contains('-')]
split_labels(labels, regex)
