        int getNextTrackNumber(boolean isStepToCenter) {
            return Math.max(Math.min((getCurrentTrackNumber() + (isStepToCenter ? 1 : -1)),
                    TRACKS_PER_DISK - 1), 0);
        }
