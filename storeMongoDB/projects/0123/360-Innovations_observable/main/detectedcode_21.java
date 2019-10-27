	public void setFilter(Predicate<? super E> filterPredicate)
	{
		final ImmutableList<E> oldList = ImmutableList.copyOf(this);

		if (filterPredicate != null)
		{
			this.filterPredicate = filterPredicate;
		}
		else
		{
			this.filterPredicate = Predicates.alwaysTrue();
		}

		refreshIndexesMap();

		ListDifference<E> difference = ListDifference.difference(oldList, ImmutableList.copyOf(this));
		CollectionChangeEvent<E> newCollectionChangeEvent = getSupport().newCollectionChangeEvent(difference);
		getSupport().fireCollectionChangeEvent(newCollectionChangeEvent);
	}
