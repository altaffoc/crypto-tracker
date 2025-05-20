const apiURL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd";

async function fetchPrices() {
  try {
    const response = await fetch(apiURL);
    const data = await response.json();

    document.getElementById("bitcoin").innerHTML = `
      <strong>Bitcoin (BTC)</strong><br/>$${data.bitcoin.usd.toLocaleString()}
    `;

    document.getElementById("ethereum").innerHTML = `
      <strong>Ethereum (ETH)</strong><br/>$${data.ethereum.usd.toLocaleString()}
    `;
  } catch (err) {
    console.error("Gagal ambil data:", err);
  }
}

fetchPrices();
setInterval(fetchPrices, 10000);
