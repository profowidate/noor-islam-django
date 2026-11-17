document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".counter-button").forEach(button => {
    let remaining = Number(button.dataset.count || 1);
    const count = button.querySelector(".count");
    button.addEventListener("click", () => {
      if (remaining > 0) remaining -= 1;
      count.textContent = remaining;
      if (remaining === 0) {
        button.classList.add("completed");
        button.querySelector("small").textContent = "أحسنت، اكتمل الذكر";
      }
    });
  });

  const tasbeehCount = document.getElementById("tasbeehCount");
  if (tasbeehCount) {
    let count = 0;
    document.getElementById("tasbeehTap").addEventListener("click", () => {
      count += 1;
      tasbeehCount.textContent = count;
    });
    document.getElementById("tasbeehReset").addEventListener("click", () => {
      count = 0;
      tasbeehCount.textContent = count;
    });
  }

  const zakatButton = document.getElementById("calculateZakat");
  if (zakatButton) {
    zakatButton.addEventListener("click", () => {
      const assets = Math.max(0, Number(document.getElementById("assets").value || 0));
      const debts = Math.max(0, Number(document.getElementById("debts").value || 0));
      const nisabRaw = document.getElementById("nisab").value;
      const net = Math.max(0, assets - debts);
      const result = document.getElementById("zakatResult");
      if (nisabRaw !== "" && net < Number(nisabRaw)) {
        result.textContent = `صافي المال: ${net.toLocaleString("ar-EG")} — أقل من النصاب المدخل.`;
      } else {
        result.textContent = `صافي المال: ${net.toLocaleString("ar-EG")} · الزكاة التقديرية: ${(net * 0.025).toLocaleString("ar-EG", {maximumFractionDigits: 2})}`;
      }
    });
  }
});
