	public boolean beginTransaction()
	{
		return transactionCount.incrementAndGet() == 1;
	}
