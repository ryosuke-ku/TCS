	public void changeVariables(Object source, Map<String, Object> variables) {
		if (variables.containsKey("selectedRecords")) {
			try {
				final JsonRootNode node = new JdomParser().parse((String) variables.get("selectedRecords"));
				selectedRecords = getListGridRecordFactory().newListGridRecords(node.getArrayNode());
			} catch (Exception e) {
				Throwables.propagate(e);
			}
		}

		if (variables.containsKey("onSelectionChanged.event")) {
			try {
				final JsonRootNode root = new JdomParser().parse((String) variables.get("onSelectionChanged.event"));
				final SelectionEvent event = getSelectionEventFactory().newSelectionEvent(root);

				for (SelectionChangedHandler handler : selectionChangedHandlers) {
					handler.onSelectionChanged(event);
				}
			} catch (Exception e) {
				Throwables.propagate(e);
			}
		}

		if (variables.containsKey("onSelectionUpdated.event")) {
			final SelectionUpdatedEvent event = new SelectionUpdatedEvent(this);

			for (SelectionUpdatedHandler handler : selectionUpdatedHandlers) {
				handler.onSelectionUpdated(event);
			}
		}

		if (variables.containsKey("onRecordDoubleClick")) {
			try {
				final JsonRootNode root = new JdomParser().parse((String) variables.get("onRecordDoubleClick.event.record"));
				final Record record = getRecordFactory().newRecord(root);
				final int recordNum = (Integer) variables.get("onRecordDoubleClick.event.recordNum");
				final ListGridField field = (ListGridField) variables.get("onRecordDoubleClick.event.field");
				final int fieldNum = (Integer) variables.get("onRecordDoubleClick.event.fieldNum");
				final RecordDoubleClickEvent event = new RecordDoubleClickEvent(this, this, record, recordNum, field, fieldNum);

				for (RecordDoubleClickHandler handler : recordDoubleClickHandlers) {
					handler.onRecordDoubleClick(event);
				}
			} catch (Exception e) {
				Throwables.propagate(e);
			}
		}

		super.changeVariables(source, variables);
	}
