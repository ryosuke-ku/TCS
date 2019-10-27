	public int lastIndexOf(Object o)
	{
		final Integer filteredIndex = indexes.inverse().get(super.lastIndexOf(o));
		return filteredIndex != null ? filteredIndex : -1;
	}
