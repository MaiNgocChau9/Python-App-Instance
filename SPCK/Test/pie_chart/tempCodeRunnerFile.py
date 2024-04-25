for slice in series.slices():
            slice.setLabel("{:.2f}%".format(100 * slice.percentage()))