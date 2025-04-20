def t_test_two_sample(df: pd.DataFrame, metric_name: str, alpha: float) -> dict:
  """
  df - датафрейм со следующими колонками:
  group - test or control
  metric - значение метрики для наблюдения
  """
  
  var_test_pvalue = levene(df[df['group']=='control'][metric_name], df[df['group']=='test'][metric_name]).pvalue # проверка на равенство дисперсий

  if var_test_pvalue < alpha:
    test_res = ttest_ind(df[df['group']=='control'][metric_name], df[df['group']=='test'][metric_name], equal_var=False)
  else:
    test_res = ttest_ind(df[df['group']=='control'][metric_name], df[df['group']=='test'][metric_name])

  pvalue = test_res.pvalue
  dof = test_res.df

  test_mean = np.mean(df[df['group']=='test'][metric_name])
  control_mean = np.mean(df[df['group']=='control'][metric_name])
  delta_mean = test_mean - control_mean


  std_agg = (np.var(df[df['group']=='control'][metric_name], ddof=1)/len(df[df['group']=='control'][metric_name]) \
                + np.var(df[df['group']=='test'][metric_name], ddof=1)/len(df[df['group']=='test'][metric_name])
  ) ** 0.5
  t_delta = sps.t.ppf(1-alpha/2, df=dof)
  delta_low_ci, delta_high_ci = delta_mean - t_delta*std_agg, delta_mean + t_delta*std_agg

  res = {'p_value': pvalue, 'test_mean': test_mean, 'control_mean': control_mean, 'delta_mean': delta_mean, 'delta_low_ci': delta_low_ci, 'delta_high_ci': delta_high_ci}

  return res
