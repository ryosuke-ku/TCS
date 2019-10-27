	public boolean addAll(int index, Collection<? extends E> c)
	{
		final int previousSize = indexes.size();
		super.addAll(indexes.get(index), c);
		return indexes.size() != previousSize;
	}
