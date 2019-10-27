	public SelectionEventFactory getSelectionEventFactory() {
		if (selectionEventFactory == null) {
			return selectionEventFactory = InjectorSingleton.get().getInstance(SelectionEventFactory.class);
		} else {
			return selectionEventFactory;
		}
	}
