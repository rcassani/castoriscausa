
How to validate and default values in matlab in a simple manner.


function plotting_modspec(Tx, Fx, Bx, freq_axis, color_axis )
%PLOTTING_MODSPEC Plot a Moduluation Spectrogram according to the
%parameters
% Tx, Vector, indicates Modulation Frequencies (x axis)
% Fx, Vector, indicates Analysis Frequencies (y axis)
% Bx, Matrix, Modulation spectrogram values
% Optional arguments
% freq_axis, Vector, 2 values, indicates the upper limits for X and Y axis
%            default [20, 20]
% color_axis, Vector, 2 values, indicates the range for color scale
%             default [0, 100]

if ~exist('freq_axis','var') || isempty(freq_axis)
    freq_axis = [20, 20];
end

if ~exist('color_axis','var') || isempty(color_axis)
    color_axis = [0, 100];
end

<center>
![Alt](http://www.castoriscausa.com/wp-content/uploads/2016/08/Capture.png "Title")
Git-Posh example</center>


function elements = tril_el( X, k )
%TRIL_EL Returns the elements of the Lower triangle in a Square matrix
%   tril_el(X,k) returns the elements on and below the kth diagonal of X.
%   See help tril for further explanation
%   If k = 0, ELEMENTS contains the Main Diagonal
%   If k = -1, ELEMENTS contains Lower Triangle except Main Diagonal

if ~exist('k','var') || isempty(k)
    k = 0;
end

elements =   X(logical(tril(ones(size(X)), k )));

end
