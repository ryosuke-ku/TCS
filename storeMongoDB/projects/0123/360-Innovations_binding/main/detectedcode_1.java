	public void undo(UndoRedoValue undoRedoValue)
	{
		getValueModel().setValue(undoRedoValue.getOldValue());
	}
