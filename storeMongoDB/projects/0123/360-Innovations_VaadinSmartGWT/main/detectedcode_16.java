	protected void fireEvent(com.google.web.bindery.event.shared.Event<?> event) {
		if (event instanceof RecordDoubleClickEvent) {
			for (RecordDoubleClickHandler handler : recordDoubleClickHandlers) {
				handler.onRecordDoubleClick((RecordDoubleClickEvent) event);
			}
		}
	}
