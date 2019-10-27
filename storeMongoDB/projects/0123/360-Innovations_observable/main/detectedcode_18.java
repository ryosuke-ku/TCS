	public int indexOf(Object o)
	{
		final Integer filteredIndex = indexes.inverse().get(super.indexOf(o));
		return filteredIndex != null ? filteredIndex : -1;
	}
