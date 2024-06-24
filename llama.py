
from clarifai.client.workflow import Workflow

# Your PAT (Personal Access Token) can be found in the Account's Security section

# Initialize the workflow_url
workflow_url = "https://clarifai.com/zqe0zx40ng15/Llama-2-tutorial/workflows/workflow-1bfdac"
text_classfication_workflow = Workflow(
    url= workflow_url , pat="f7d7faaa3c8943d0920c39c081e520d6"
)
result = text_classfication_workflow.predict_by_bytes(b"I hate you", input_type="text")
print(result.results[0].outputs[0].data)
