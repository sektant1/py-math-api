document.addEventListener("DOMContentLoaded", () => {
	const form = document.getElementById("calc-form");
	const exprInput = document.getElementById("expr");
	const btn = document.getElementById("btn");
	const output = document.getElementById("output");

	function showAlert(kind, message) {
		output.innerHTML = `
			<div class="alert alert-${kind} mb-0" role="alert">
				${message}
			</div>
		`;
	}

	form.addEventListener("submit", async (e) => {
		e.preventDefault();

		const expr = exprInput.value.trim();
		if (!expr) {
			showAlert("warning", "Digite uma expressao antes de calcular.");
			return;
		}

		btn.disabled = true;
		btn.textContent = "Calculando...";
		output.innerHTML = "";

		try {
			const res = await fetch("/api/calc", {
				method: "POST",
				headers: { "Content-Type": "application/json" },
				body: JSON.stringify({ expr })
			});

			const data = await res.json().catch(() => ({}));

			if (!res.ok) {
				showAlert("danger", data.error ?? "Erro ao calcular");
				return;
			}

			showAlert("success", `<strong>Resultado:</string> ${data.result}`);
		} catch {
			showAlert("danger", "Nao consegui conectar na API, veja se o server esta rodando.");

		} finally {
			btn.disabled = false;
			btn.textContent = "Calcular";
		}
	});
});
