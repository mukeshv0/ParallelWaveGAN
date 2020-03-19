import torch
import torch.nn.functional as F


class HingeLoss(torch.nn.Module):

    def __init__(self):
        super(HingeLoss, self).__init__()

    def forward(self, y_hat, is_real):
        """Calculate forward propagation.

        Args:
            y_hat (Tensor): predictions
            is_real (bool): is the label "real"

        Returns:
            Tensor: Hinge loss value 
        """
        if is_real:
            return F.relu(1 - y_hat).mean()
        else:
            return F.relu(1 + y_hat).mean()