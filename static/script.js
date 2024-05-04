function playerMove(index) {
    fetch(`/move/${index}`)
        .then(response => response.json())
        .then(data => {
            updateBoard(data.cell_values);
            if (data.oppo) {
                document.getElementById('status').textContent = `Winner: Player`;
            } else if (data.play) {
                document.getElementById('status').textContent = "Ai won the match";
            }
            else if (data.tie) {
                document.getElementById('status').textContent = "It's a Draw";
            }
            else{
                setTimeout(triggerAIMove,780);
            }
        })
        .catch(error => console.error('Error:', error));
    }

    function updateBoard(cellValues) {
        let ind=0;
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                let text = cellValues[i][j];
                document.getElementById(ind).textContent = text;
                ind=ind+1;
            }
        }
    }

function triggerAIMove(event){
    fetch(`/aiMove`)
        .then(response => response.json())
        .then(data => {
            updateBoard(data.cell_values);
            if (data.oppo) {
                document.getElementById('status').textContent = `Winner: Player`;
            } else if (data.play) {
                document.getElementById('status').textContent = "Ai won the match";
            }
            else if (data.tie) {
                document.getElementById('status').textContent = "It's a Draw";
            }
        })
        .catch(error => console.error('Error:', error));
    }


    function reset(){
        fetch(`/reset`)
        .then(response => response.json)
        .then(data => {
            updateBoard(data.cell_values);
        })
        .catch(error => console.error('Error:', error));
    }
