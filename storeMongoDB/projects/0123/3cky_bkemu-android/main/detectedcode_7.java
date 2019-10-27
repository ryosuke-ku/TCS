        void setCurrentTrack(int trackNumber, FloppyDriveSide trackSide) {
            if (isDebugEnabled) {
                d(TAG, "set track: " + trackNumber + ", side: " + trackSide);
            }
            this.currentTrackNumber = trackNumber;
            this.currentTrackSide = trackSide;
            // OnFloppyDriveTrackChanged listeners notify if disk image mounted
            if (isDiskImageMounted()) {
                for (OnFloppyDriveTrackChanged listener : trackChangedListeners) {
                    listener.onFloppyDriveTrackChanged(trackNumber, trackSide);
                }
            }
        }
