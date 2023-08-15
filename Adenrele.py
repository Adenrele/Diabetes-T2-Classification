import numpy as np

def show_values(axs, orient="v", space=.01):
    """
    Display values on seaborn barplots.

    Args:
        axs (Axes object or ndarray of Axes objects): The axes or array of axes for barplots.
        orient (str): Orientation of the barplots ("v" for vertical, "h" for horizontal).
        space (float): Space between value text and bar.

    Returns:
        None
    """
    # Code adapted from https://www.statology.org/seaborn-barplot-show-values/

    def _single(ax):
        if orient == "v":
            # Loop through the patches of each bar
            for p in ax.patches:
                _x = p.get_x() + p.get_width() / 2
                _y = p.get_y() + p.get_height() + (p.get_height() * 0.01)
                value = '{:.2f}'.format(p.get_height())  # Format value to display
                ax.text(_x, _y, value, ha="center")  # Display value at the appropriate position
        elif orient == "h":
            # Loop through the patches of each bar
            for p in ax.patches:
                _x = p.get_x() + p.get_width() + float(space)
                _y = p.get_y() + p.get_height() - (p.get_height() * 0.5)
                value = '{:.2f}'.format(p.get_width())  # Format value to display
                ax.text(_x, _y, value, ha="left")  # Display value at the appropriate position

    if isinstance(axs, np.ndarray):
        # If axs is an array of axes
        for idx, ax in np.ndenumerate(axs):
            _single(ax)
    else:
        # If axs is a single axis
        _single(axs)

def check_balance(dataframe, feature_or_label, threshold=0.4):
    """
    Check if a dataset is balanced for a specified class.

    Args:
        dataframe (DataFrame): The pandas DataFrame containing the data.
        feature_or_label (str): The column name of the feature or label to check for balance.
        threshold (float): The threshold for balance check (default is 0.4).

    Returns:
        None
    """
    
    # Calculate the counts of class values
    class_counts = dataframe[feature_or_label].value_counts()
    total = len(dataframe)

    # Calculate the percentage of each class
    class_percentages = (class_counts / total) * 100

    print("Class percentages:")
    for class_value, percentage in class_percentages.items():
        print("Class {}: {:.3f}%".format(class_value, percentage))

    # Calculate the mean percentage and threshold range
    mean_percentage = class_percentages.mean()
    lower_threshold = mean_percentage - threshold
    upper_threshold = mean_percentage + threshold

    # Check if the dataset is balanced based on the threshold range
    is_balanced = all(lower_threshold <= percentage <= upper_threshold for percentage in class_percentages)
    
    if is_balanced:
        print("This is a balanced dataset with respect to {}.".format(feature_or_label))
    else:
        print("This is an unbalanced dataset with respect to {}.".format(feature_or_label))