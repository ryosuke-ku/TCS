	public void redo()
	{
		UndoRedoOperation pollFirst = getRedoableOperations().pollFirst();
		if (pollFirst != null)
		{
			getOperations().addLast(pollFirst);
			pollFirst.redo();
		}
	}
