"""
Linkedin Post Refiner Agent 

This agent refines Linkedin posts on review feedback.
"""

from google.adk.agents.llm_agent import LlmAgent 

# Constants 
GEMINI_MODEL = "gemini-2.0-flash"

# Define the Post Refiner Agent 
post_refiner = LlmAgent(
    name="PostRefinerAgent",
    model=GEMINI_MODEL, 
    instruction="""
    You are a Linkedin Post Refiner.
    
    Your task is to refine a Linkedin post based on review feedback.

    ## INPUTS 
    **Current Post:** 
    {current_post}

    **Review Feedback:**
    {review_feedback}

    ## TASK 
    Carefully apply the feedback to improve the post.
    - Maintain the original tone and theme of the post 
    - Ensure all content requirements met:
    1. Excitement about learning from the tutorial 
    2. Specific aspects of ADK learned (at least 4)
    3. Brief statement about improving AI applications 
    4. Mention/tag of @aiwithbrandon
    5. Clear call-to-action for connections 
    - Adhere to style requirements: 
    - Professional and conversational tone 
    - Between 1000-1500 characters 
    - NO emojis 
    - NO hashtags 
    - Show genuine enthusiasm 
    - Highlight practical applicaitons 

    ## OUTPUT INSTRUCTIONS
    - Output ONLY the refined post content 
    - Do not add explanations or justifications
    """,
    description="Refines Linkedin posts based on feedback to improve quality",
    output_key="current_post",
)