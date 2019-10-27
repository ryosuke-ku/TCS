	public HandlerRegistration addRecordDoubleClickHandler(final RecordDoubleClickHandler handler) {
		recordDoubleClickHandlers.add(handler);
		return new HandlerRegistration() {
			@Override
			public void removeHandler() {
				recordDoubleClickHandlers.remove(handler);
			}
		};
	}
