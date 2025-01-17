Name:		texlive-ctanify
Version:	44129
Release:	2
Summary:	Prepare a package for upload to CTAN
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/ctanify
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctanify.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctanify.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-ctanify.bin = %{EVRD}

%description
Given a list of filenames, ctanify creates a tarball (a .tar.gz
file) with the files laid out in CTAN's preferred structure.
The tarball additionally contains a ZIP (.zip) file with copies
of all files laid out in the standard TeX Directory Structure
(TDS), which may be used by those intending to install the
package, or by those who need to incorporate it in a
distribution. (The TDS ZIP file will be installed in the CTAN
install/ tree.).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/ctanify
%{_texmfdistdir}/scripts/ctanify/ctanify
%doc %{_texmfdistdir}/doc/latex/ctanify/README
%doc %{_texmfdistdir}/doc/latex/ctanify/ctanify.pdf
%doc %{_mandir}/man1/ctanify.1*
%doc %{_texmfdistdir}/doc/man/man1/ctanify.man1.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/ctanify/ctanify ctanify
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
