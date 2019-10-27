	public static <E> ObservableUnsafeFilteredSubList<E> of(ObservableList<? super E> source, Predicate<? super E> filterPredicate)
	{
		return new ObservableUnsafeFilteredSubList(source, filterPredicate);
	}
