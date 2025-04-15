function plotData(x, y, plotTitle, xLabel, yLabel, lineStyle)
    % Check if x and y have the same length
    if length(x) ~= length(y)
        error('Vectors x and y must be of the same length.');
    end
    
    % Create the plot
    figure;
    plot(x, y, lineStyle, 'LineWidth', 2);
    
    % Add title and labels
    title(plotTitle, 'FontSize', 14, 'FontWeight', 'bold');
    xlabel(xLabel, 'FontSize', 12);
    ylabel(yLabel, 'FontSize', 12);
    
    % Add grid for better readability
    grid on;
    
    % Display the plot
    disp('Plot successfully generated.');
end