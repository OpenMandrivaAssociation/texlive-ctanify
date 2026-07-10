%global tl_name ctanify
%global tl_revision 44129

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.9.1
Release:	%{tl_revision}.1
Summary:	Prepare a package for upload to CTAN
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/ctanify
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ctanify.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ctanify.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(ctanify.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Given a list of filenames, ctanify creates a tarball (a .tar.gz file)
with the files laid out in CTAN's preferred structure. By default this
tarball additionally contains a ZIP (.zip) file with copies of all files
laid out in the standard TeX Directory Structure (TDS), which may be
used by those intending to install the package, or by those who need to
incorporate it in a distribution. (The TDS ZIP file will be installed in
the CTAN install/ tree.) Given that CTAN and TeX Live are not fond of
.tds.zip files for small and/or otherwise straightforward packages,
ctanify has now been provided with an option that prevents the creation
and inclusion of such a .tds.zip file.

