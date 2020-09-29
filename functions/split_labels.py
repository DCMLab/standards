import re, logging

from split_alternatives import split_alternatives

def split_labels(df, regex, column='label', cols={}, dropna=False, logger=None, **kwargs):
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
    logger : :obj:`logging.Logger`, optional
        Pass Logger object if you don't want to use the RootLogger.

    Example
    -------

    .. code-block:: python
        import pandas as pd
        from get_regex import get_regex
        labels = pd.read_csv('labels.csv')
        regex = get_regex()
        split_labels(labels, regex)
    """
    if not logger:
        logger = logging.getLogger()

    assert regex.__class__ == re.compile('').__class__, "Compile regular expression using re.compile()"
    df = df.copy()
    if df[column].isna().any():
        if dropna:
            logger.debug(f"Removing NaN values from label column {column}...")
            df = df[df[column].notna()]
        else:
            logger.warning(f"{column} contains NaN values.")

    logger.debug(f"Splitting alternative annotations...")
    split_alternatives(df=df, column=column, logger=logger)

    logger.debug("Applying RegEx to labels...")
    spl = df[column].str.extract(regex, expand=True)
    features = regex.groupindex.keys()
    df = pd.concat([df, spl[features]], axis=1)
    mistakes = spl.isna().apply(all, axis=1) & df[column].notna()
    if mistakes.any():
        logger.warning(f"The following chords could not be parsed:\n{df.loc[mistakes, :column]}")
    return df
