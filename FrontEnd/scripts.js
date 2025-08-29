let currentLanguage = 'SV';
let expandedStates = [];




document.addEventListener('DOMContentLoaded', function () {
    start();
});

function start() {
	toggleLanguage(); 
	document.getElementById("expandButton").addEventListener("click", expandAll);
	document.getElementById("collapseButton").addEventListener("click", collapseAll);
	document.getElementById("project_list").addEventListener("click", getData);
	document.getElementById("project_info").addEventListener("click", displayInformation);
	document.getElementById("search_tips").addEventListener("click", displayTips);
}


function getData() {
    fetch('top_documents.json')
        .then(response => response.json())
        .then(projects => displayProjects(projects))
        .catch(error => console.error('Error fetching projects:', error));
}

function toggleLanguage() {
    const languageToggles = document.querySelectorAll('.language-toggle');

    currentLanguage = currentLanguage === 'EN' ? 'SV' : 'EN';

    languageToggles.forEach(element => {
        element.classList.remove('bold');
    });

    const selectedToggle = document.querySelector(`.language-toggle[data-lang="${currentLanguage}"]`);
    selectedToggle.classList.add('bold');

    const aboutListHeading = document.getElementById('about_list_heading');
    aboutListHeading.innerHTML = currentLanguage === 'EN' ? 'About the list' : 'Om listan';

    const projectListHeading = document.getElementById('project_list_heading');
    projectListHeading.innerHTML = currentLanguage === 'EN' ? 'Project List' : 'Projektlista';

    const tipsListHeading = document.getElementById('tips_list_heading');
    tipsListHeading.innerHTML = currentLanguage === 'EN' ? 'Search tips' : 'Söktips';

    getData(); 
}

function collapseAll() {
	expandedStates =  [];
	updateProjectRows();
}

function expandAll() {
	projectRows = document.querySelectorAll('.project-row');

	projectRows.forEach((row, index) => {
		expandedStates.push(index);
	});
	
	updateProjectRows();
}


function getProjectTitle(project) {
    const projectTitle = currentLanguage === 'SV' ? project.projectTitleSv : project.projectTitleEn;
	if (!projectTitle) {
      return 	currentLanguage === 'EN' ? project.projectTitleSv : project.projectTitleEn;	
	}
	return projectTitle;
}

function getProjectAbstract(project) {
    const projectAbstract =  currentLanguage === 'SV' ? project.projectAbstractSv : project.projectAbstractEn;
	if (!projectAbstract) {
      return 	currentLanguage === 'EN' ? project.projectAbstractSv : project.projectAbstractEn;	
	}
	return projectAbstract;
}

function getFundingOrganization(project) {
    return currentLanguage === 'SV' ? project.fundingOrganisationNameSv : project.fundingOrganisationNameEn;
}

function getCoordinatingOrganization(project) {
    return currentLanguage === 'SV' ? project.coordinatingOrganisationNameSv : project.coordinatingOrganisationNameEn;
}

function getPrincipalInvestigatorName(project) {
    const principalInvestigator = project.peopleList.find(person => person.roleEn === 'Principal Investigator');
    return principalInvestigator ? principalInvestigator.fullName : '';
}

function getPrincipalInvestigatorOrcID(project) {
    const principalInvestigator = project.peopleList.find(person => person.roleEn === 'Principal Investigator');
    return principalInvestigator ? principalInvestigator.orcId : '';
}

function getSCBs(project) {
    const scbsArray = project.scbs || [];

    const formattedSCBs = scbsArray.map(scb => {
        const scbName = currentLanguage === 'SV' ? scb.scb5NameSv : scb.scb5NameEn;
        return `[${scb.scb5Id}: ${scbName}]`; 
    });

    return formattedSCBs.join('\n');
}

function createHeaderRow(projects) {
    const headerRowContainer = document.createElement('div');
    headerRowContainer.className = 'header-row-container';

    const headerRow = document.createElement('div');
    headerRow.className = 'header-row';
    headerRow.innerHTML = `
        <p><strong> </strong></p>
        <p><strong>ProjectID:</strong></p>
        <p><strong>Coordinating Organization:</strong></p>
        <p><strong>Start:</strong></p>
        <p><strong>End:</strong></p>
    `;
    headerRowContainer.appendChild(headerRow);

    return headerRowContainer;
}

function createProjectRow(project, index) {
    const projectRow = document.createElement('div');
	
	const summaryRow = document.createElement('div');
    let title_num = index+1;

    summaryRow.className = 'summary-row';
    summaryRow.innerHTML = `
        <p> </p>
        <p>${project.projectId}</p>
        <p>${getCoordinatingOrganization(project)}</p>
        <p>${project.fundingStartDate} - ${project.fundingEndDate}</p>
    `;

    const titleRow = document.createElement('div');
	titleRow.className = 'title-row';
	
    titleRow.innerHTML = `
        <h3>${title_num}. ${getProjectTitle(project)}</h3>
    `;

    projectRow.className = 'project-row';
	
	projectRow.addEventListener('click', function () {
        toggleProjectRow(index);
    });
	
    projectRow.appendChild(titleRow)
	projectRow.appendChild(summaryRow)
	


    return projectRow;
}

function createProjectDetails(project, index) {
    const projectDetailsContainer = document.createElement('div');
    const projectAbstractHeader = document.createElement('div');
    projectAbstractHeader.className = 'project-details';
	/* If you want the PI name:
    projectAbstractHeader.innerHTML = `
        <h><strong>Project Abstract:</strong></h>
        <p>${getProjectAbstract(project)}</p>
        <h><strong>Principal Investigator Name (ORCID):</strong></h>
        <p>${getPrincipalInvestigatorName(project)}  (${getPrincipalInvestigatorOrcID(project)})</p>
        <h><strong>Funding Organization:</strong></h>
        <p>${getFundingOrganization(project)}</p>
        <h><strong>List of SCBS:</strong></h>
        <p>${getSCBs(project)}</p>
        <p><a href=https://www.vr.se/english/swecris.html?project/${project.projectId}#/project/${project.projectId} target="_blank">Go to source record at Swecris</a></p>
    `;
    */
	    projectAbstractHeader.innerHTML = `
        <h><strong>Project Abstract:</strong></h>
        <p>${getProjectAbstract(project)}</p>
        <h><strong>Funding Organization:</strong></h>
        <p>${getFundingOrganization(project)}</p>
        <h><strong>SCB classifications:</strong></h>
        <p>${getSCBs(project)}</p>
        <p><a href=https://www.vr.se/english/swecris.html#/project/${project.projectId} target="_blank">Go to source record at Swecris</a></p>
    `;

        
    // Initially hide the details if not expanded
    if (!expandedStates.includes(index)) {
        projectAbstractHeader.style.display = 'none';
    }

    projectDetailsContainer.appendChild(projectAbstractHeader);

    return projectDetailsContainer;
}

function toggleProjectRow(index) {
    const indexExists = expandedStates.indexOf(index);

    if (indexExists !== -1) {
        expandedStates.splice(indexExists, 1);
    } else {
        expandedStates.push(index);
    }

    updateProjectRows();
}

function updateProjectRows() {
    const projectRows = document.querySelectorAll('.project-row');

    projectRows.forEach((row, index) => {
        if (expandedStates.includes(index)) {
            row.classList.add('expanded');
        } else {
            row.classList.remove('expanded');
        }
    });

    const projectDetailsContainers = document.querySelectorAll('.project-details');
    projectDetailsContainers.forEach((container, index) => {
        if (expandedStates.includes(index)) {
            container.style.display = 'block';
        } else {
            container.style.display = 'none';
        }
    });
}

function displayProjects(projects) {
    const projectsList = document.getElementById('projects-list');
    projectsList.innerHTML = '';

    /*const headerRowContainer = createHeaderRow(projects);
    projectsList.appendChild(headerRowContainer);*/

    let i = 0;
    projects.forEach(project => {
        const projectElement = createProjectRow(project, i);
        const projectDetails = createProjectDetails(project, i);
		
        const projectContainer = document.createElement('div');
		projectContainer.className = 'single-project-container';
		
        projectContainer.appendChild(projectElement);
        projectContainer.appendChild(projectDetails);
		projectsList.appendChild(projectContainer);
        i++;
    });
}

function displayInformation() {
	const infoDiv = document.getElementById('projects-list');
    let infoFile = 'about.html';
    infoFile = currentLanguage === 'EN' ? 'about.html' : 'om.html';
	fetch(infoFile)
	.then(response => response.text())
	.then(text => infoDiv.innerHTML = text)
/*     infoDiv.innerHTML = `
        <h><strong>About the list:</strong></h>
        <p>blah blah</p>

    `;*/

}

function displayTips() {
	const infoDiv = document.getElementById('projects-list');
    let infoFile = 'search_tips.html';
    infoFile = currentLanguage === 'EN' ? 'search_tips.html' : 'soktips.html';
	fetch(infoFile)
	.then(response => response.text())
	.then(text => infoDiv.innerHTML = text)
/*     infoDiv.innerHTML = `
        <h><strong>About the list:</strong></h>
        <p>blah blah</p>

    `;*/

}

