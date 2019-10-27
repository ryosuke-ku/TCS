	public boolean removeAll(Collection<?> c)
	{
		final int previousSize = indexes.size();
		super.removeAll(c);
		return indexes.size() != previousSize;
	}
