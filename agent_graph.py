from pydantic import BaseModel
from typing import TypedDict
# In production, we import StateGraph from langgraph.graph
# from langgraph.graph import StateGraph, END

class AutoDevState(TypedDict):
    issue_text: str
    code_generated: str
    test_results: str
    iteration: int
    success: bool

class AutoDevGraph:
    """
    Simulates a LangGraph cyclic agent workflow:
    Planner -> Coder -> Tester -> (If Fail, loop back to Coder) -> Reviewer -> END
    """
    def __init__(self, max_iterations=3):
        self.max_iterations = max_iterations

    def run(self, issue_text: str):
        print(f"\n[Graph] Starting AutoDev loop for issue: '{issue_text}'")
        state: AutoDevState = {
            "issue_text": issue_text,
            "code_generated": "",
            "test_results": "",
            "iteration": 0,
            "success": False
        }
        
        while state["iteration"] < self.max_iterations and not state["success"]:
            state["iteration"] += 1
            print(f"\n--- Iteration {state['iteration']} ---")
            
            # Agent 1: Coder
            print("[Agent: Coder] Writing code based on issue...")
            state["code_generated"] = f"def solve():\n    return 'fix for {issue_text[:10]}'"
            
            # Agent 2: Tester (using DockerSandbox in real app)
            print("[Agent: Tester] Running tests in isolated environment...")
            if state["iteration"] == 1:
                print("[Agent: Tester] Tests Failed! SyntaxError on line 2.")
                state["test_results"] = "Fail"
            else:
                print("[Agent: Tester] Tests Passed!")
                state["test_results"] = "Pass"
                state["success"] = True
                
        # Agent 3: Reviewer
        if state["success"]:
            print("\n[Agent: Reviewer] Code is solid. Proceeding to PR creation.")
        else:
            print("\n[Agent: Reviewer] Max iterations reached. Failing gracefully.")
        
        return state
