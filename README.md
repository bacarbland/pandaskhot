# pandaskhot
Generalization of one hot encoding (pandas.get_dummies) for multiple categorical columns having the same possible labels

## Parameters
        df : pandas.DataFrame
            The source DataFrame
        cols: Listor, numpy.Array or pandas.Series
            A List like object with the name of the 
        dummy_na: Bool = False
            Add a column to indicate NaNs, if False NaNs are ignored.
## Returns
        DataFrame
            A DataFrame with the affected columns rounded to the specified
            number of decimal places.

## See Also
        Pandas.get_dummies: Convert categorical variable into dummy/indicator variables.

## Examples
        >>> df = pd.DataFrame({'foo_1': ['a', 'b', 'a', 'h', 'g'], 'foo_2': ['b', 'a', 'c', 'g', 'c'],
        ...                    'foo_3': ['e', 'c', 'f', 'c', 'h'],'foo_4': ['f', 'e', 'b', 'a', 'c']})
        >>> df
          foo_1 foo_2 foo_3 foo_4
        0     a     b     e     f
        1     b     a     c     e
        2     a     c     f     b
        3     h     g     c     a
        4     g     c     h     c
        >>> kHot(df,df.columns)
           a  b  c  e  f  g  h
        0  1  1  0  1  1  0  0
        1  1  1  1  1  0  0  0
        2  1  1  1  0  1  0  0
        3  1  0  1  0  0  1  1
        4  0  0  2  0  0  1  1
        
        >>> kHot(df,df.columns,dummy_na=True)
           a  b  c  e  f  g  h  nan
        0  1  1  0  1  1  0  0    0
        1  1  1  1  1  0  0  0    0
        2  1  1  1  0  1  0  0    0
        3  1  0  1  0  0  1  1    0
        4  0  0  2  0  0  1  1    0

       
       
