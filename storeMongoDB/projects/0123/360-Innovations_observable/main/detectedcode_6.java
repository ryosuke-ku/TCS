	public List<E> subList(int fromIndex, int toIndex)
	{
		final ObservableList<E> subList = (ObservableList<E>) super.subList(indexes.get(fromIndex), indexes.get(toIndex));

		subList.addCollectionChangeListener(new CollectionChangeHandler());
		return new ObservableUnsafeFilteredSubList<E>(subList, filterPredicate);
	}
