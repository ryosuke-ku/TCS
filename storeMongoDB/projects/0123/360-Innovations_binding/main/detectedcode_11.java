	protected boolean isCurrentlyInTransaction()
	{
		return transactionCount.get() > 0;
	}
