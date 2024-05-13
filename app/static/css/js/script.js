document.addEventListener('DOMContentLoaded', () => {
    const inputText = document.getElementById('inputText');
    const summarizeBtn = document.getElementById('summarizeBtn');
    const summarizedText = document.getElementById('summarizedText');

    summarizeBtn.addEventListener('click', async () => {
        const text = inputText.value;
        const response = await fetch('/summarize', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: new URLSearchParams({ text })
        });
        const data = await response.json();
        summarizedText.textContent = data.summarized_text;
    });
});
