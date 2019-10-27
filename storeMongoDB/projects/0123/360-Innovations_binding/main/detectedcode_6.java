	public SavePoint createSavePoint()
	{
		// We need to clear the redoable operations
		getRedoableOperations().clear();
		UndoRedoOperation peekLast = getOperations().peekLast();

		DefaultSavePoint savePoint = new DefaultSavePoint(peekLast);
		getSavePoints().add(savePoint);

		return savePoint;
	}
