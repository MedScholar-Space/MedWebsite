from django import template
from django.apps import apps

register = template.Library()

@register.filter(name='get_answer')
def get_answer(answer_ids, target_id):
    """
    Custom template filter to retrieve a specific answer object 
    from a list of answer IDs.
    
    Args:
        answer_ids (list): List of answer IDs
        target_id (int): ID of the specific answer to retrieve
    
    Returns:
        Answer object or None
    """
    # Import the Answer model dynamically to avoid circular imports
    Answer = apps.get_model('Quiz', 'Answer')
    
    try:
        # Find the specific answer that matches the target ID
        return Answer.objects.get(id=target_id)
    except Answer.DoesNotExist:
        return None