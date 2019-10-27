	public boolean retainAll(Collection<?> c)
	{
		final int previousSize = indexes.size();
		super.retainAll(c);
		return indexes.size() != previousSize;
	}
