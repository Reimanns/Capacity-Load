import streamlit as st
import streamlit.components.v1 as components

# Optionally, display the logo with st.image if you have it locally:
st.image("citadel_logo.png", width=200)

# Embed the entire HTML/JS code as a multi-line string.
html_code = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8" />
  <title>Labor Capacity Dashboard</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 40px;
    }
    .logo {
      display: block;
      margin: 0 auto 20px auto;
      max-height: 100px;
    }
    h1 {
      text-align: center;
      margin-bottom: 10px;
    }
    .chart-container {
      width: 1000px;
      height: 600px;
      margin-bottom: 50px;
    }
    select {
      font-size: 16px;
      padding: 5px;
      margin-bottom: 10px;
    }
  </style>
</head>
<body>



<h1>Capacity-Load By Discipline</h1>

<!-- Dropdown for discipline selection -->
<label for="disciplineSelect">Select Discipline: </label>
<select id="disciplineSelect"></select>

<!-- Chart container -->
<div class="chart-container">
  <canvas id="myChart"></canvas>
</div>

<script>
// ------------------------------------------------------------------------
// 1) DEFINE YOUR DATA
// ------------------------------------------------------------------------

const projects = [
  {
    number: "P7578",
    customer: "ADFAM",
    aircraftModel: "A340",
    scope: "Center Gear Replacement",
    induction: "2025-02-10",
    delivery: "2025-02-17",
    Maintenance: 688,
    Interiors: 0,
    Avionics: 0,
    SheetMetal: 0,
    FinishPaint: 0,
    Engineering: 0,
    Upholstery: 0,
    Cabinetry: 0
  },
  {
    number: "P7476",
    customer: "GE",
    aircraftModel: "747-400",
    scope: "Multi Check, AD's & SB's",
    induction: "2025-02-18",
    delivery: "2025-04-03",
    Maintenance: 4955,
    Interiors: 100,
    Avionics: 0,
    SheetMetal: 0,
    FinishPaint: 0,
    Engineering: 0,
    Upholstery: 0,
    Cabinetry: 0
  },
  {
    number: "P7591",
    customer: "Freedom II",
    aircraftModel: "757-200",
    scope: "B Check, AD's & SB's",
    induction: "2025-02-23",
    delivery: "2025-03-02",
    Maintenance: 871.5,
    Interiors: 0,
    Avionics: 0,
    SheetMetal: 0,
    FinishPaint: 0,
    Engineering: 0,
    Upholstery: 0,
    Cabinetry: 0
  },
  {
    number: "P7560",
    customer: "BEFO",
    aircraftModel: "737",
    scope: "96mnth Check",
    induction: "2025-03-23",
    delivery: "2025-06-15",
    Maintenance: 4038,
    Interiors: 1921,
    Avionics: 0,
    SheetMetal: 0,
    FinishPaint: 0,
    Engineering: 8,
    Upholstery: 14,
    Cabinetry: 0
  },
  {
    number: "P7517",
    customer: "Parallel",
    aircraftModel: "757-200",
    scope: "Interior Mod",
    induction: "2025-04-15",
    delivery: "2025-08-31",
    Maintenance: 584,
    Interiors: 5997,
    Avionics: 7114,
    SheetMetal: 1885,
    FinishPaint: 4920,
    Engineering: 0,
    Upholstery: 6885,
    Cabinetry: 2272
  },
  {
    number: "P7561",
    customer: "L3-FBI",
    aircraftModel: "757-200",
    scope: "Maintenance & Interior Mod",
    induction: "2025-07-31",
    delivery: "2025-10-14",
    Maintenance: 6882,
    Interiors: 1029,
    Avionics: 276,
    SheetMetal: 90,
    FinishPaint: 116,
    Engineering: 244,
    Upholstery: 0,
    Cabinetry: 228
  },
  {
    number: "P7426",
    customer: "Celestial",
    aircraftModel: "757",
    scope: "Maintenance & Interior Mod",
    induction: "2025-02-06",
    delivery: "2025-03-28",
    Maintenance: 0,
    Interiors: 2840,
    Avionics: 0,
    SheetMetal: 0,
    FinishPaint: 953,
    Engineering: 0,
    Upholstery: 1025,
    Cabinetry: 100
  },
  {
    number: "P7592",
    customer: "LJ Aviation",
    aircraftModel: "",
    scope: "GOGO WAP",
    induction: "2025-02-23",
    delivery: "2025-03-06",
    Maintenance: 0,
    Interiors: 0,
    Avionics: 0,
    SheetMetal: 0,
    FinishPaint: 0,
    Engineering: 0,
    Upholstery: 0,
    Cabinetry: 0
  },
  {
    number: "P7392",
    customer: "L3-FBI",
    aircraftModel: "757",
    scope: "Maintenance & Interior Mod",
    induction: "2025-04-20",
    delivery: "2025-05-20",
    Maintenance: 0,
    Interiors: 695,
    Avionics: 300,
    SheetMetal: 90,
    FinishPaint: 16,
    Engineering: 220,
    Upholstery: 0,
    Cabinetry: 240
  }
];

const potentialProjects = [
  {
    number: "P7580",
    customer: "Polaris",
    aircraftModel: "B737",
    scope: "144 Mo. Check",
    induction: "2025-09-01",
    delivery: "2025-11-10",
    Maintenance: 4162,
    Interiors: 3783,
    Avionics: 1135,
    SheetMetal: 2270,
    FinishPaint: 0,
    Engineering: 0,
    Upholstery: 0,
    Cabinetry: 0
  }
];

const projectsActual = [
  {
    number: "P7578",
    customer: "ADFAM",
    aircraftModel: "A340",
    scope: "Center Gear Replacement",
    induction: "2025-02-10",
    delivery: "2025-02-17",
    Maintenance: 458.9,
    Interiors: 5.59,
    Avionics: 0,
    SheetMetal: 65.4,
    FinishPaint: 0,
    Engineering: 0,
    Upholstery: 0,
    Cabinetry: 0
  },
  {
    number: "P7476",
    customer: "GE",
    aircraftModel: "747-400",
    scope: "Multi Check, AD's & SB's",
    induction: "2025-02-18",
    delivery: "2025-04-03",
    Maintenance: 132.74,
    Interiors: 9.16,
    Avionics: 32.66,
    SheetMetal: 0,
    FinishPaint: 0,
    Engineering: 0,
    Upholstery: 0,
    Cabinetry: 0
  },
  {
    number: "P7591",
    customer: "Freedom II",
    aircraftModel: "757-200",
    scope: "B Check, AD's & SB's",
    induction: "2025-02-23",
    delivery: "2025-03-02",
    Maintenance: 427.35,
    Interiors: 24,
    Avionics: 98.29,
    SheetMetal: 166,
    FinishPaint: 0,
    Engineering: 0,
    Upholstery: 12.5,
    Cabinetry: 0
  },
  {
    number: "P7560",
    customer: "BEFO",
    aircraftModel: "737",
    scope: "96mnth Check",
    induction: "2025-03-23",
    delivery: "2025-06-15",
    Maintenance: 0,
    Interiors: 0,
    Avionics: 0,
    SheetMetal: 0,
    FinishPaint: 0,
    Engineering: 0,
    Upholstery: 0,
    Cabinetry: 0
  },
  {
    number: "P7517",
    customer: "Parallel",
    aircraftModel: "757-200",
    scope: "Interior Mod",
    induction: "2025-04-15",
    delivery: "2025-08-31",
    Maintenance: 0,
    Interiors: 309.74,
    Avionics: 298.06,
    SheetMetal: 12.32,
    FinishPaint: 89.67,
    Engineering: 0,
    Upholstery: 607.42,
    Cabinetry: 102.75
  },
  {
    number: "P7561",
    customer: "L3-FBI",
    aircraftModel: "757-200",
    scope: "Maintenance & Interior Mod",
    induction: "2025-07-31",
    delivery: "2025-10-14",
    Maintenance: 0,
    Interiors: 0,
    Avionics: 0,
    SheetMetal: 0,
    FinishPaint: 0,
    Engineering: 0,
    Upholstery: 0,
    Cabinetry: 0
  },
  {
    number: "P7426",
    customer: "Celestial",
    aircraftModel: "757",
    scope: "Maintenance & Interior Mod",
    induction: "2025-02-06",
    delivery: "2025-03-28",
    Maintenance: 1857.8,
    Interiors: 3187.8,
    Avionics: 489.91,
    SheetMetal: 743.65,
    FinishPaint: 265.76,
    Engineering: 0,
    Upholstery: 216.51,
    Cabinetry: 284.07
  },
  {
    number: "P7592",
    customer: "LJ Aviation",
    aircraftModel: "",
    scope: "GOGO WAP",
    induction: "2025-02-23",
    delivery: "2025-03-06",
    Maintenance: 0,
    Interiors: 0,
    Avionics: 125.73,
    SheetMetal: 0,
    FinishPaint: 0,
    Engineering: 0,
    Upholstery: 0,
    Cabinetry: 0
  },
  {
    number: "P7392",
    customer: "L3-FBI",
    aircraftModel: "757",
    scope: "Maintenance & Interior Mod",
    induction: "2025-04-20",
    delivery: "2025-05-20",
    Maintenance: 0,
    Interiors: 0,
    Avionics: 0,
    SheetMetal: 0,
    FinishPaint: 0,
    Engineering: 0,
    Upholstery: 0,
    Cabinetry: 0
  }
];

const departmentCapacities = [
  { name: "Interiors",    headcount: 14,  key: "Interiors" },
  { name: "Finish",       headcount: 4,   key: "FinishPaint" },
  { name: "Cabinetry",    headcount: 2,   key: "Cabinetry" },
  { name: "Upholstery",   headcount: 6,   key: "Upholstery" },
  { name: "Avionics",     headcount: 7,   key: "Avionics" },
  { name: "Sheet Metal",  headcount: 10,  key: "SheetMetal" },
  { name: "Engineering",  headcount: 3,   key: "Engineering" }
];

const PRODUCTIVITY_FACTOR = 0.8;

// ------------------------------------------------------------------------
// 2) HELPER FUNCTIONS
// ------------------------------------------------------------------------

function parseDate(dateStr) {
  if (dateStr.includes("/")) {
    const [m, d, y] = dateStr.split("/");
    return new Date(+y, +m - 1, +d);
  } else {
    return new Date(dateStr);
  }
}

function getWeekList() {
  let minDate = null;
  let maxDate = null;

  function expandDates(arr) {
    for (const p of arr) {
      const ind = parseDate(p.induction);
      const del = parseDate(p.delivery);
      if (!minDate || ind < minDate) minDate = ind;
      if (!maxDate || del > maxDate) maxDate = del;
    }
  }

  expandDates(projects);
  expandDates(potentialProjects);
  expandDates(projectsActual);

  const start = new Date(minDate);
  while (start.getDay() !== 1) {
    start.setDate(start.getDate() - 1);
  }

  const weeks = [];
  const current = new Date(start);
  while (current <= maxDate) {
    weeks.push(new Date(current));
    current.setDate(current.getDate() + 7);
  }

  return weeks.map(d => d.toISOString().slice(0, 10));
}

function computeWeeklyLoadsDetailed(projectsArray, disciplineKey, weekLabels) {
  const weeklyTotal = new Array(weekLabels.length).fill(0);
  const breakdown = weekLabels.map(() => []);

  for (const p of projectsArray) {
    const totalHours = p[disciplineKey] || 0;
    if (totalHours === 0) continue;

    const startDate = parseDate(p.induction);
    const endDate = parseDate(p.delivery);

    let startIndex = -1;
    let endIndex = -1;

    for (let i = 0; i < weekLabels.length; i++) {
      const labelDate = new Date(weekLabels[i]);
      if (labelDate >= startDate && startIndex === -1) {
        startIndex = i;
      }
      if (labelDate <= endDate) {
        endIndex = i;
      }
    }

    if (startIndex !== -1 && endIndex !== -1 && endIndex >= startIndex) {
      const numWeeks = endIndex - startIndex + 1;
      const hoursPerWeek = totalHours / numWeeks;

      for (let w = startIndex; w <= endIndex; w++) {
        weeklyTotal[w] += hoursPerWeek;
        breakdown[w].push({
          customer: p.customer,
          hours: hoursPerWeek
        });
      }
    }
  }

  return { weeklyTotal, breakdown };
}

function computeWeeklyLoadsActual(projectsArray, disciplineKey, weekLabels) {
  const weeklyTotal = new Array(weekLabels.length).fill(0);
  const breakdown = weekLabels.map(() => []);
  const today = new Date();

  for (const p of projectsArray) {
    const totalHours = p[disciplineKey] || 0;
    if (totalHours === 0) continue;

    const startDate = parseDate(p.induction);
    const plannedEndDate = parseDate(p.delivery);

    let actualEndDate;
    if (startDate > today) {
      actualEndDate = plannedEndDate;
    } else {
      actualEndDate = plannedEndDate < today ? plannedEndDate : today;
    }

    if (actualEndDate < startDate) continue;

    let startIndex = -1;
    let endIndex = -1;

    for (let i = 0; i < weekLabels.length; i++) {
      const labelDate = new Date(weekLabels[i]);
      if (labelDate >= startDate && startIndex === -1) {
        startIndex = i;
      }
      if (labelDate <= actualEndDate) {
        endIndex = i;
      }
    }

    if (startIndex !== -1 && endIndex !== -1 && endIndex >= startIndex) {
      const numWeeks = endIndex - startIndex + 1;
      const hoursPerWeek = totalHours / numWeeks;

      for (let w = startIndex; w <= endIndex; w++) {
        weeklyTotal[w] += hoursPerWeek;
        breakdown[w].push({
          customer: p.customer,
          hours: hoursPerWeek
        });
      }
    }
  }

  return { weeklyTotal, breakdown };
}

// ------------------------------------------------------------------------
// 3) MAIN LOGIC
// ------------------------------------------------------------------------

const weekLabels = getWeekList();

const disciplineDataMapConfirmed = {};
departmentCapacities.forEach(dept => {
  const { weeklyTotal, breakdown } = computeWeeklyLoadsDetailed(
    projects,
    dept.key,
    weekLabels
  );
  const weeklyCapacity = dept.headcount * 40 * PRODUCTIVITY_FACTOR;
  const capacityArray = weeklyTotal.map(() => weeklyCapacity);

  disciplineDataMapConfirmed[dept.key] = {
    disciplineName: dept.name,
    weeklyTotal,
    capacityArray,
    breakdown
  };
});

const disciplineDataMapPotential = {};
departmentCapacities.forEach(dept => {
  const { weeklyTotal, breakdown } = computeWeeklyLoadsDetailed(
    potentialProjects,
    dept.key,
    weekLabels
  );
  disciplineDataMapPotential[dept.key] = {
    disciplineName: dept.name,
    weeklyTotal,
    breakdown
  };
});

const disciplineDataMapActual = {};
departmentCapacities.forEach(dept => {
  const { weeklyTotal, breakdown } = computeWeeklyLoadsActual(
    projectsActual,
    dept.key,
    weekLabels
  );
  disciplineDataMapActual[dept.key] = {
    disciplineName: dept.name,
    weeklyTotal,
    breakdown
  };
});

const disciplineSelect = document.getElementById('disciplineSelect');
departmentCapacities.forEach(dept => {
  const option = document.createElement('option');
  option.value = dept.key;
  option.textContent = dept.name;
  disciplineSelect.appendChild(option);
});
disciplineSelect.value = "Interiors";

const ctx = document.getElementById('myChart').getContext('2d');
let currentKey = disciplineSelect.value;

function getConfirmedData(key) {
  return disciplineDataMapConfirmed[key];
}
function getPotentialData(key) {
  return disciplineDataMapPotential[key];
}
function getActualData(key) {
  return disciplineDataMapActual[key];
}

let currentConfirmed = getConfirmedData(currentKey);
let currentPotential = getPotentialData(currentKey);
let currentActual    = getActualData(currentKey);

const myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: weekLabels,
    datasets: [
      {
        label: currentConfirmed.disciplineName + " Load (hrs)",
        data: currentConfirmed.weeklyTotal,
        borderColor: '#003366',
        backgroundColor: 'rgba(0, 51, 102, 0.2)',
        borderWidth: 2,
        fill: true,
        tension: 0.1
      },
      {
        label: currentConfirmed.disciplineName + " Capacity (hrs)",
        data: currentConfirmed.capacityArray,
        borderColor: '#FF0000',
        backgroundColor: 'rgba(255, 0, 0, 0.2)',
        borderWidth: 2,
        fill: false,
        borderDash: [5,5],
        tension: 0.1
      },
      {
        label: currentConfirmed.disciplineName + " Potential (hrs)",
        data: currentPotential.weeklyTotal,
        borderColor: 'green',
        backgroundColor: 'rgba(0, 255, 0, 0.2)',
        borderWidth: 2,
        fill: true,
        tension: 0.1
      },
      {
        label: currentConfirmed.disciplineName + " Actual (hrs)",
        data: currentActual.weeklyTotal,
        borderColor: 'orange',
        backgroundColor: 'rgba(255, 165, 0, 0.2)',
        borderWidth: 2,
        fill: true,
        tension: 0.1
      }
    ]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    interaction: {
      mode: 'index',
      intersect: false
    },
    scales: {
      x: {
        title: {
          display: true,
          text: 'Week Starting'
        }
      },
      y: {
        title: {
          display: true,
          text: 'Hours'
        },
        beginAtZero: true
      }
    },
    plugins: {
      title: {
        display: true,
        text: `Weekly Load vs. Capacity - ${currentConfirmed.disciplineName}`
      }
    },
    onClick: (evt, activeElements) => {
      if (!activeElements || activeElements.length === 0) return;
      const { datasetIndex, index: weekIndex } = activeElements[0];
      if (datasetIndex === 1) {
        alert("You clicked on the Capacity line; no project breakdown.");
        return;
      }
      let breakdownArr, label;
      if (datasetIndex === 0) {
        breakdownArr = getConfirmedData(currentKey).breakdown[weekIndex];
        label = "Confirmed";
      } else if (datasetIndex === 2) {
        breakdownArr = getPotentialData(currentKey).breakdown[weekIndex];
        label = "Potential";
      } else {
        breakdownArr = getActualData(currentKey).breakdown[weekIndex];
        label = "Actual";
      }
      if (!breakdownArr || breakdownArr.length === 0) {
        alert(`No ${label} project hours in this week.`);
        return;
      }
      let msg = `Drilldown for week: ${weekLabels[weekIndex]}\n` +
                `Discipline: ${getConfirmedData(currentKey).disciplineName}\n` +
                `Type: ${label}\n\n`;
      breakdownArr.forEach(b => {
        msg += `${b.customer}: ${b.hours.toFixed(1)} hrs\n`;
      });
      alert(msg);
    }
  }
});

disciplineSelect.addEventListener('change', function() {
  currentKey = this.value;
  currentConfirmed = getConfirmedData(currentKey);
  currentPotential = getPotentialData(currentKey);
  currentActual    = getActualData(currentKey);
  myChart.data.datasets[0].label = currentConfirmed.disciplineName + " Load (hrs)";
  myChart.data.datasets[0].data  = currentConfirmed.weeklyTotal;
  myChart.data.datasets[1].label = currentConfirmed.disciplineName + " Capacity (hrs)";
  myChart.data.datasets[1].data  = currentConfirmed.capacityArray;
  myChart.data.datasets[2].label = currentConfirmed.disciplineName + " Potential (hrs)";
  myChart.data.datasets[2].data  = currentPotential.weeklyTotal;
  myChart.data.datasets[3].label = currentConfirmed.disciplineName + " Actual (hrs)";
  myChart.data.datasets[3].data  = currentActual.weeklyTotal;
  myChart.options.plugins.title.text =
    `Weekly Load vs. Capacity - ${currentConfirmed.disciplineName}`;
  myChart.update();
});
</script>
</body>
</html>
"""

# Render the HTML code in the Streamlit app.
components.html(html_code, height=800)
